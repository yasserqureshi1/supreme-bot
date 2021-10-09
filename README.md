# Supreme Bot

This is a basic Supreme bot that was created in the [Create a Supreme Bot]() video.

## Installation
Install the dependencies using the command in Terminal or Command Prompt:
```
pip install -r requirements.txt
```

## Usage

To use the bot, please fill in your details in the `config.py` file.
The table below outlines what needs to be defined in the file.

Element | Format | Description
--------|--------|-------------
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
```CARD_TYPE``` | String | Card type - either "Visa", "American Express", "Mastercard", or "Solo"
```EXP_MONTH``` | String/Integer | Two digit expiry month 

Once these elements have been defined, run the script and it will start waiting/looking for the product, and purchase it once available.
