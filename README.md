## Screenshot Verification

This open-source tool is specifically designed to verify the absence of error messages after performing a screenshot verification. If an error message is found, details that are available are also displayed.

Simply pass a single screenshot image or a directory of images to the tool and it will extract the required information for you.

### Requirements

- Python 3.x
- [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract)
- [OpenCV-Python](https://github.com/opencv/opencv-python)

### Example

Import both Verify and Classifier from verify.py in your Python file:

```python
import os
from verify import Verify, Classifier

screenshots = os.listdir('screenshots')

if __name__ == '__main__':
    print('Verifying screenshots...')
    for file in screenshots:
        output = Verify('./screenshots/' + file).verify_screenshot()
        Classifier(output, file).classify()
    print('Done!')
```
Example output when running against the provided \screenshots\ folder:
```
[ERROR] [error (1).png] Windows Boot Manager Error
[ERROR] [error (1).png] > File: \Windows\system32\winload.exe
[ERROR] [error (1).png] > Status: Oxc000000e
[ERROR] [error (1).png] > Info: The selected entry could not be loaded because the application is
[ERROR] [error (2).png] A problem has been detected Error
[ERROR] [error (3).png] Windows Boot Manager Error
[ERROR] [error (3).png] > File: \Windows\system32\ntoskrn1.exe
[ERROR] [error (3).png] > Status: 0xc0000221
[ERROR] [error (3).png] > Info: The operating system couldn't be loaded because the kernel is
[ERROR] [error (4).png] PC Ran Into a Problem Error       
[ERROR] [error (4).png] > Stop code: CRITICAL PROCESS DIED
[ERROR] [error (5).png] Repair Your Computer Error
[SUCCESS] [false (1).png] No errors detected
[SUCCESS] [false (2).png] No errors detected
[SUCCESS] [false (3).png] No errors detected
```