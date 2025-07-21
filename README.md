# Simple-Python-Encoder-Decoder
This is a simple Python tool to encode/decode your passwords, private keys etc. It can be used in Python or as an exe file for Windows/Linux/Mac.

<img width="472" height="449" alt="image" src="https://github.com/user-attachments/assets/413efb2f-59f2-42ba-85ac-e4ff8b285cb5" />


You can run the simple_encoder_decoder.py directly with Python or create your own exe file for Windows/Linux/Mac:
```
pip install pyinstaller
pyinstaller --onefile c:/your_path/simple_encoder_decoder.py
```

How you can use the lib in your Python projects to encode/decode texts:
```
import simple_encoder_decoder as sed

shift = 5
seed = 12345
charset = sed.generate_charset(seed)
shift_pattern_num = 20  # Max 100!
shift_pattern = get_shift_pattern(shift, seed, shift_pattern_num)

input_text: str = "Hello World"

encoded_text = sed.encode(input_text, charset, shift_pattern)
decoded_text = sed.decode(encoded_text, charset, shift_pattern)
print(input_text, encoded_text, decoded_text)
```

Another variant(less procedural):
```
import simple_encoder_decoder as sed

seed = 12345
charset = sed.generate_charset(seed)
shift_pattern = [2, 5, 6, 8, 25, 86]  # Max value is 100!

input_text: str = "Hello World"

encoded_text = sed.encode(input_text, charset, shift_pattern)
decoded_text = sed.decode(encoded_text, charset, shift_pattern)
print(input_text, encoded_text, decoded_text)
```

USE ON YOUR OWN RISK!
