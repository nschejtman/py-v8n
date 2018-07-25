<p align="center">
  <img src="./docs/assets/logo.png" alt="py-v8n" />
</p>

<p align="center">
The ultimate <b>Python</b> validation library you've ever needed.<br/>
Dead simple fluent API. Customizable. Reusable.
</p>

[![Build Status](https://travis-ci.org/nschejtman/py-v8n.svg?branch=master)](https://travis-ci.org/nschejtman/py-v8n)
[![CircleCI](https://circleci.com/gh/nschejtman/py-v8n.svg?style=shield)](https://circleci.com/gh/nschejtman/py-v8n)
[![codecov](https://codecov.io/gh/nschejtman/py-v8n/branch/master/graph/badge.svg)](https://codecov.io/gh/nschejtman/py-v8n)

```python
v8n()
  .int_()
  .between(0, 100)
  .even()
  .not_().equal(32)
  .test(74) # true
```
## What is it?
`py-v8n` is a reusable fluent validation library. 

## Installation
```shell
pip install py-v8n
```  

## Usage

```python
from py_v8n import v8n

# Create a validator
hello_validator = v8n()\
    .str_()\
    .first("H")\
    .last("o")\
    
# Check values
hello_validator.test("Hello") # True
hello_validator.test("Good bye") # False
 
```