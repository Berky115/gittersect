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



## Command-line instructions:

In order to run gittersect navigate to the gittersect directory and run using 2 user names. Use details below

```
Type:        instancemethod
String form: <bound method GittersectService.compare_users of <__main__.GittersectService object at 0x10f2b0710>>
File:        ./gittersect
Line:        32

Usage:       gittersect USER1 USER2
             gittersect --user1 USER1 --user2 USER2
```

You may also add the gittersect utility to your path in order to run from anywhere.

## Commands
-- --help : See command-line documentation for use
