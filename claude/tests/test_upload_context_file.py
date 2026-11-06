import importlib.util
import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch


SCRIPT = Path(__file__).parents[1] / "skills/create-dealroom/scripts/upload_context_file.py"
spec = importlib.util.spec_from_file_location("upload_context_file", SCRIPT)
upload = importlib.util.module_from_spec(spec)
spec.loader.exec_module(upload)


class UploadContextFileTests(unittest.TestCase):
    def test_puts_original_bytes_with_signed_headers(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.pdf"
            path.write_bytes(b"original-pdf-bytes")
            session = {
                "uploadUrl": "https://bucket.s3.amazonaws.com/object?signature=secret",
                "uploadHeaders": [{"key": "Content-Type", "value": "application/pdf"}],
            }

            transferred = []

            def receive(request, timeout):
                transferred.append(request.data.read())
                response = MagicMock()
                response.__enter__.return_value.status = 200
                return response

            with patch.object(upload.urllib.request, "urlopen", side_effect=receive) as urlopen:
                upload.upload_file(path, session)

            request = urlopen.call_args.args[0]
            self.assertEqual(request.get_method(), "PUT")
            self.assertEqual(request.get_header("Content-type"), "application/pdf")
            self.assertEqual(request.get_header("Content-length"), "18")
            self.assertEqual(transferred, [b"original-pdf-bytes"])

    def test_rejects_non_https_upload_url(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "example.txt"
            path.write_bytes(b"original")
            session = {"uploadUrl": "http://example.com/upload", "uploadHeaders": []}
            with patch.object(upload.urllib.request, "urlopen") as urlopen:
                with self.assertRaisesRegex(ValueError, "HTTPS"):
                    upload.upload_file(path, session)
            urlopen.assert_not_called()


if __name__ == "__main__":
    unittest.main()
