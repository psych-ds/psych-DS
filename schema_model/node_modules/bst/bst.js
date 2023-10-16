(function(root) {
  'use strict';

  function BST() {
    if (!(this instanceof BST)) {
      return new BST();
    }

    this.root = null;
  }

  BST.prototype.push = function(value) {
    if (!this.root) {
      this.root = new BST.Node(value);
    }

    var currentNode = this.root;
    var newNode = new BST.Node(value);

    while(currentNode) {
      if (value < currentNode.value) {
        if (!currentNode.left) {
          currentNode.left = newNode;
          break;
        } else {
          currentNode = currentNode.left;
        }
      } else {
        if (!currentNode.right) {
          currentNode.right = newNode;
          break;
        } else {
          currentNode = currentNode.right;
        }
      }
    }
  };

  BST.prototype.invert = function(root) {
    if (!root) {
      return false;
    }

    var tmp = root.left;
    root.left = root.right;
    root.right = tmp;

    if (root.left) {
      this.invert(root.left);
    }
    if (root.right) {
      this.invert(root.right);
    }
  };

  BST.Node = function Node(value) {
    if (!(this instanceof Node)) {
      return new Node(value);
    }

    this.value = value;
    this.left = null;
    this.right = null;
  };

  if (typeof exports !== 'undefined') {
    if (typeof module !== 'undefined' && module.exports) {
      exports = module.exports = BST;
    }
    exports.BST = BST;
  } else if (typeof define === 'function' && define.amd) {
    define([], function() {
      return BST;
    });
  } else {
    root.BST = BST;
  }

})(this);
