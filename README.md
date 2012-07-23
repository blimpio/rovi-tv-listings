#rovi-tv-listings
**Python Wrapper for Rovi TV Listings API**

---

Rovi TV Listings returns international television schedules, plus data and images for programs and celebrities.

* **services**: Television service offerings for an area.
* **service_details**: Channel lineup offered by a television service.
* **linear_schedule**: TV listings with detailed program information.
* **grid_schedule**: TV listings designed for the space limitations of a grid.
* **program_details**: Information about a series, episode, or program, plus a schedule of upcoming broadcasts.
* **celebrity_details**: Information about a celebrity, plus a schedule of upcoming broadcasts the celebrity appears in.

## Examples
```
from rovi.tv_listings import TVListings

tv_listings = TVListings(api_key='CHANGE-ME')
print tv_listings.services(postal_code='00911', country_code='US')
print tv_listings.service_details(service_id='361032')
print tv_listings.service_details(service_id='361032')
print tv_listings.grid_schedule(service_id='361032')
print tv_listings.program_details(program_id='4258917')
print tv_listings.celebrity_details(name_id='100614')
```

## API Key
[http://developer.rovicorp.com/page/Get_Started](http://developer.rovicorp.com/page/Get_Started)

## Notice
This is a totally un-official project and Rovi Corporation is not involved in any way. We made this to make our work easier and decided to share it.

## Bug tracker
Have a bug? Please [create an issue here on GitHub](https://github.com/GetBlimp/rovi-tv-listings/issues)!

## License
All of rovi-tv-listings is licensed under the MIT license.

Copyright (c) 2012 Giovanni Collazo

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
