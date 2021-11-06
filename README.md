# Supreme Bot

This is a basic Supreme bot that was created in the [Create a Supreme Bot]() video.

## About the Project
This project contains the source code of a basic open-source Supreme bot that was created in the YouTube video [here](). The bot is able to search for an item, choose a colour and size, and proceed to checkout. 

Feel free to contribute by forking the project and opening a Pull Request.

## Contents

- [About the Project](#about-the-project)
- [Set-Up](#set-up)
- [Usage](#usage)
- [Issues](#issues)
- [License](#license)


## Set-Up

1. Ensure you have Python 3+ installed. You can install it at this link [here](https://www.python.org/downloads/).
2. Clone or Download the repository.
    - Clone:
    ```
    git clone 
    ```
    - Download: Clock on the green `Code` button and click on `Download ZIP`. Then unzip this folder.
3. Install the dependencies using the following command in Terminal or Command Prompt:
```
pip3 install -r requirements.txt
```
4. Download a Chrome Driver if you haven't already. This is used to perform browser automation and can be downloaded [here](https://chromedriver.chromium.org/downloads). 
5. Edit `config.py` file with your details including the path to the Chrome Driver
6. Run `bot.py` file
```
python3 bot.py
```

## Usage

To use the bot, please fill in your details in the `config.py` file.
The table below outlines what needs to be defined in the file.

Element | Format | Description
--------|--------|-------------
```CHROME_DRIVER_PATH``` | String | Path to Chrome Driver
```KEYWORDS```| String | Words that are in the name of the item
```COLOUR``` | String | Colour of the item
```SIZE``` | String | Size of the item (if not applicable or any, leave empty)
```NAME``` | String | Full name of the buyer
```EMAIL``` | String | Email of the buyer
```TELE``` | String/Integer | Buyer's phone number
```ADDRESS_1``` | String | First line of the address
```ADDRESS_2``` | String | Second line of the address
```ADDRESS_3``` | String | Third line of the address
```CITY``` | String | City for delivery
```POSTCODE``` | String | The postcode for delivery 
```CARD_NUMBER``` | String/Integer | Card number for payment
```CVV``` |  String/Integer | CVV for the associated card
```CARD_TYPE``` | String | Card type 
```EXP_MONTH``` | String/Integer | Two digit expiry month 
```EXP_YEAR``` | String/Integer | Four digit expiry year 

Once these elements have been defined, run the script and it will start waiting/looking for the product, and purchase it once available.

## Issues

Please open an issue [here](https://github.com/yasserqureshi1//issues/new).

## License

Distributed under the MIT License. See `LICENSE` for more information. 

## Contact

For help, join my Discord Server [here](https://discord.gg/D8kfJ4pt3m).