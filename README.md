## Implementation
To implement the gittersect utility follow these steps...

- Clone repository from git:
```
git clone git@github.com:Berky115/gittersect.git
```

- install necessary python packages for your environment using [pip](https://pypi.org/project/pip/)
:
```
pip install -r requirements.txt 
```

- run gittersect.py with desired usernames

```
python gittersect.py user1 user2
```

- or run the gittersect executable in the same manner. You may also add this utility to your path.

```
./gittersect user1 user2
```

Note: gittersect supports (and recommends) passing a github access token to the program. This can be done by setting the environmental variable GITHUB_ACCESS_TOKEN

```
GITHUB_ACCESS_TOKEN=token_value python gittersect/gittersect.py user1 user2
```

## Testing:
To run the utilities test suit. Navigate to and run the gittersect_test.ut.py file. NOTE you will need to have run gittersect.py to generate the gittersect.pyc file used in these tests.

```
python gittersect/gittersect_test.ut.py   
```

## Command-line instructions:

In order to run gittersect navigate to the gittersect directory and run using 2 user names. User details below

```
Usage:       gittersect USER1 USER2
             gittersect --user1 USER1 --user2 USER2
```

## Commands
-- --help : See command-line documentation for use
