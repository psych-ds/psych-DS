# bst

> A basic [Binary Search Tree](https://en.wikipedia.org/wiki/Binary_search_tree) implementation in JavaScript.

# Install

```bash
npm install bst
```

```bash
bower install bst
```

# Usage

```javascript
var bst = require('bst');

var bst = new BST();
bst.push(3);
bst.push(2);
bst.push(4);
bst.push(1);
bst.push(5);
bst.push(2);
console.log(bst.root);

/*
{
  "value": 3,
  "left": {
    "value": 2,
    "left": {
      "value": 1,
      "left": null,
      "right": null
    },
    "right": {
      "value": 2,
      "left": null,
      "right": null
    }
  },
  "right": {
    "value": 3,
    "left": null,
    "right": {
      "value": 4,
      "left": null,
      "right": {
        "value": 5,
        "left": null,
        "right": null
      }
    }
  }
}
*/

bst.invert(bst.root);

console.log(bst.root);

/*
{
  "value": 3,
  "left": {
    "value": 3,
    "left": {
      "value": 4,
      "left": {
        "value": 5,
        "left": null,
        "right": null
      },
      "right": null
    },
    "right": null
  },
  "right": {
    "value": 2,
    "left": {
      "value": 2,
      "left": null,
      "right": null
    },
    "right": {
      "value": 1,
      "left": null,
      "right": null
    }
  }
}
*/
```

# Test

```bash
npm test
```

# License

MIT
