## [datamodel-code-generator](https://github.com/koxudaxi/datamodel-code-generator/) reproducible example for [issue #2330](https://github.com/koxudaxi/datamodel-code-generator/issues/2330)

|Inputs|Outputs|
|-|-|
|[inputs/commons.schema.json](inputs/commons.schema.json)|[outputs/commons_schema.py](outputs/commons_schema.py)|
|[inputs/products.schema.json](inputs/products.schema.json)|[outputs/products_schema.py](outputs/products_schema.py)|
|[inputs/products_unified.schema.json](inputs/products_unified.schema.json)|[outputs/products_unified_schema.py](outputs/products_unified_schema.py)|

### Description of the problem

- We define an array under `#/$defs/$defaultArray' in [inputs/commons.schema.json](inputs/commons.schema.json)
- We `ref` the array `commons.schema.json#/$defs/$defaultArray` in [inputs/products.schema.json](inputs/products.schema.json)

  Then we add other keywords to better define our object (which is [allowed](https://json-schema.org/draft/2020-12/json-schema-core#section-8.2.3.1-1)).

- We have [inputs/products_unified.schema.json](inputs/products_unified.schema.json) which is supposed to be equivalent to [inputs/products.schema.json](inputs/products.schema.json), just without any `$ref`


### Goal

We want to generate a **Pydantic V2** model for `products` with both:

- The properties of referenced array.
- The properties defined by other keywords specified in the object.


### Issue

`datamodel-code-generator` doesn't merge the properties of the referenced array with the properties given by the additional keywords, which is [allowed by the jsonschema specification](https://json-schema.org/draft/2020-12/json-schema-core#section-8.2.3.1-1).

The products model's `root`, is supposed to be a **list of [1, 100] string elements** (as generated in [products unified](outputs/products_unified_schema.py)) is instead a **generic list of [1, 100] elements** ([product](outputs/products_schema.py)).

### Generate models

```sh
$ pip install -r requirements.txt
$ datamodel-codegen
```