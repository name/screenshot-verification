import os
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class Verify:
    def __init__(self, screenshot_path):
        self.screenshot_path = screenshot_path

    def verify_screenshot(self):
        # print('Checking Screenshot: ' + self.screenshot_path)
        img = cv2.imread(self.screenshot_path)
        text = pytesseract.image_to_string(img)
        return text

    def verify_screenshots(self):
        screenshots = os.listdir(self.screenshot_path)
        for file_name in screenshots:
            print(file_name)
            self.verify_screenshot(file_name)


class Classifier:
    def __init__(self, text: str, file: str):
        self.text = text
        self.file = file

    def classify(self):
        Log = Logger()
        error = False
        # print('DEBUG: ' + self.text + '\n\n')
        for line in self.text.splitlines():
            if "File: " in line:
                Log.error(self.file, "Windows Boot Manager Error")
                error = True
                errors = self.diagnose("Windows Boot Manager")
                for error in errors:
                    Log.error(self.file, '> ' + error)
            if "Your PC ran" in line:
                Log.error(self.file, "PC Ran Into a Problem Error")
                error = True
                errors = self.diagnose("PC Ran Into a Problem")
                for error in errors:
                    Log.error(self.file, '> ' + error)
            if "Inaccessible boot device" in line:
                Log.error(self.file, "Inaccessible boot device Error")
                error = True
                Log.error(self.file, "Inaccessible boot device")
            if "Critical process died" in line:
                Log.error(self.file, "Critical process died Error")
                error = True
                Log.error(self.file, "Critical process died")
            if "A problem has been detected" in line:
                Log.error(self.file, "A problem has been detected Error")
                error = True
            if "Safe Mode with Net" in line:
                Log.error(self.file, "Repair Your Computer Error")
                error = True

        if not error:
            Log.success(self.file, 'No errors detected')

    def diagnose(self, type):
        if type == "Windows Boot Manager":
            errors = []
            for line in self.text.splitlines():
                if "File: " in line:
                    errors.append(line)
                if "Status: " in line:
                    errors.append(line)
                if "Info: " in line:
                    errors.append(line)
            return errors
        if type == "PC Ran Into a Problem":
            errors = []
            for line in self.text.splitlines():
                if "Stop code" in line:
                    errors.append(line)
            return errors


class Logger:
    def __init__(self):
        pass

    def success(self, file, message):
        print('[SUCCESS] [' + file + '] ' + message)

    def error(self, file, message):
        print('[ERROR] [' + file + '] ' + message)
