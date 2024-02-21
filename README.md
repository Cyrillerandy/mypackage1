# mypackage1 

This package was created as an illustration of creating custom python packages.
It sorts an array and returns the top n largest numbers in descending order.

# build this package locally
`python setup.py sdist`

# Installing the package from github
`pip install git+https://github.com/Cyrillerandy/mypackage1.git`

# updating the package from github
`pip install --upgrade git+https://githib.com/Cyrillerandy/mypackage1.git`

## Usage

```python
from mypackage1 import myModule1

# returns the top n values 
myModule1.top_n([8, 2, 3, 7, 4], 3)

# Expected output
[8, 7, 4]
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[COR](https://choosealicense.com/licenses/cor/)