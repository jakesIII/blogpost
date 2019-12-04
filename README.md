# Thy Blog Post | https://thyblogpost.herokuapp.com/
#### An app that creates blog posts and displays random quotes, 28/10/2019

#### Built by **Jacques Kiruma**
## Nature
Thy Blog Post is  a personal blogging website where you can create and share your opinions and other users can read and comment on them. Additionally, it has a feature that displays random quotes to inspire your users.
## Setup
* Clone this repo to your desktop
* run this in your terminal "git remove set-url" if you wish to have it into your repository
* create a directory for this project
* run "pip install" in your terminal to install python packages and "pip update" to update the packages.
* run "atom ." in you terminal

## Bugs
No known bugs.

## Behavior driven devlopment (BDD)
| Element           | Action               | Behaviour                   |
| ------------------|:--------------------:| ---------------------------:|
| registration form |Key in details        | puts info in db             |
| login form        |Key in details        |Authenticates users          |
| post form         |Key in details        |puts post in db              |
| update post form  |Key in details        |updates the post             |
| delete post       |Key in details        |deletes post in db           |
| navbar            |select options        |navigates to specific route  |
| random quote      |refresh               |Displays random quote        |


## Technologies
* Flask
* Python3.6
* Bootstrap
* SQLAlchemy


## Support and contact details
For feedback , complaints or queries :
Email: jayruma@yahoo.com
### License

MIT License

Copyright (c) 2019 Jacques Kiruma III

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
