import os
from verify import Verify, Classifier

screenshots = os.listdir('screenshots')

if __name__ == '__main__':
    print('Verifying screenshots...')
    for file in screenshots:
        output = Verify('./screenshots/' + file).verify_screenshot()
        Classifier(output, file).classify()
    print('Done!')
