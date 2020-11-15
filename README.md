# Supreme Bot

This is a basic Supreme bot that is still in development. 
Feel free to make any pull requests and improve this.

## Installation
Below is a list of the packages needed:
```
selenium
requests
dotenv
```
You can install these using the command:
```
pip install -r requirements.txt
```

## Usage

To use the bot, please fill in your details in the ```.env``` file.
The table below outlines what needs to be defined in the file.

Element | Format | Description
--------|--------|-------------
```KEYWORDS```| String | Words that are in the name of the item
```COLOUR``` | String | The colour of the item
```SIZE``` | String | The size of the item (if not applicable or you don't mind, leave empty)
```NAME``` | String | The full name of the buyer
```EMAIL``` | String | The email of the buyer
```TELE``` | String/Integer | The buyer's phone number
```ADDRESS_1``` | String | The first line of the address
```ADDRESS_2``` | String | The second line of the address
```ADDRESS_3``` | String | The third line of the address
```CITY``` | String | The city for delivery
```POSTCODE``` | String | The postcode for delivery 
```CARD_NUMBER``` | String/Integer | The card number for payment
```CVV``` |  String/Integer | The CVV for the associated card
```CARD_TYPE``` | String | The card type - either "Visa", "American Express", "Mastercard", or "Solo"
```EXP_MONTH``` | String/Integer | Two digit expiry month 

Once these elements have been defined, run the script at it will start waiting/looking for the product, and purchase it once available.

## To Do

- [ ] Fix Captcha
- [ ] Better UI
- [ ] Continue to find item if not available
- [ ] Better error messages if keywords or colour not found
- [ ] No size or any size option