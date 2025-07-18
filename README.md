# Simple-Python-Encoder-Decoder
<img width="627" height="388" alt="image" src="https://github.com/user-attachments/assets/77e5cd70-b50d-47b1-b278-9769f020d925" />

You can run the simple_encoder_decoder.py directly with Python or create your own exe file for Windows/Linux/Mac:
```
pip install pyinstaller
pyinstaller --onefile cc:/your_path/simple_encoder_decoder.py
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
