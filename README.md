# Simple-Python-Encoder-Decoder
This is a simple Python tool to encode/decode your passwords, private keys etc. It can be used in Python or as an exe file for Windows/Linux/Mac.

<img width="472" height="449" alt="image" src="https://github.com/user-attachments/assets/413efb2f-59f2-42ba-85ac-e4ff8b285cb5" />


You can run the simple_encoder_decoder.py directly with Python or create your own exe file for Windows/Linux/Mac:
```
pip install pyinstaller
pyinstaller --onefile c:/your_path/simple_encoder_decoder.py
```

There are 3 main functions which you can use in your projects to encode/decode texts:
```
import simple_encoder_decoder as sed

shift = 5
charset = sed.generate_charset(12345)

my_text: str = "Hello World"

encoded_text = sed.encode(my_text, charset, shift)
decoded_text = sed.decode(encoded_text, charset, shift)
```

USE ON YOUR OWN RISK!
