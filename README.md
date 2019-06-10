### gittersect
gittersect is a command-line utility that allows a user to compare two github login names and determin what followers they have in common

## implementation
To implement the gittersect utility follow these steps...

- Clone repository from git:
```
git clone git@github.com:Berky115/gittersect.git
```

- install necessary python packages for your environment (virtualEnv is recommended):
    ```
    pip install -r requirements.txt 
    ```

- run gittersect.py with desired user names
```
python gittersect user1 user2
```

Note: gittersect supports (and recommends) passing a github access token to the program. This can be done by setting the environmental variable GITHUB_ACCESS_TOKEN

```
GITHUB_ACCESS_TOKEN=token_value python gittersect/gittersect.py user1 user2
```

## Testing:
To run the utilities test suit. Navigate to the gittersect_test.ut.py file and run with no arguments
```
python gittersect/gittersect_test.ut.py   
```



## Set to Command-line:

```
chmod +x gittersect.py
mv gittersect.py gittersect
```

add to path

```
mkdir -p ~/bin
cp gittersect ~/bin
export PATH=$PATH":$HOME/bin"
```

## Commands
-- --help : See command-line documentation for use