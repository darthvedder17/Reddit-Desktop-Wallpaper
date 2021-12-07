Steps to run this script on : 
1. Make a virtualenv using ```virtualenv env``` Note : Make sure you have pip installed or go to https://pip.pypa.io/en/stable/installation/ for help
2. Activate the virtualenv using ```env\Scripts\activate``` if you're on Windows.
3. Install the requirements file using ```pip install -r requirements.txt```
4. Make a file ```credentials.py``` in the same directory where the pull is taken.
5. Go to Reddit, (the old Reddit) , Preferences -> Apps -> Create App
6. Add the three variables in your ```credentials.py``` file as follows 
 ```
    my_client_secret  = 'asdsacsdacsdcasd'
    my_client_id = 'asdcacdas'
    my_user_agent = 'demo'
    
 ```   
7. Run the program ```python reddit.py```. Note : You can also specify the download location using ``` python reddit.py --dl "{Specify Path Here}"```
