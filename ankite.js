class Node {
    constructor(val) {
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

class Tree {
    constructor() {
        this.root = null;
        this.foundNode = null;
    }

    insert = (val, par, lor) => {
        var newNode = new Node(val);
        if (!this.root) {
            this.root = newNode;
        } else {

            this.searchNode(this.root, par)
            var reqNode = this.foundNode;

            if (reqNode) {
                if (reqNode[lor]) {
                    console.log('Not the leaf node')
                    return;
                } else {
                    reqNode[lor] = newNode;
                }
                this.foundNode = null
            } else {
                console.log('Can\'t find the parent Node')
                return;
            }
        }
    }
    DFS() {
        let result = [];

        function search(node) {
            if (!node)
                return;

            result.push(node.val)
            node.left && search(node.left);
            node.right && search(node.right);
        }
        search(this.root)
        return result
    }
    searchNode = (root, node) => {
        if (!root) {
            return null;
        }
        if (root.val === node) {

            this.foundNode = root;

        } else {
            this.searchNode(root.left, node)
            this.searchNode(root.right, node)

        }


    }

    BFS = () => {
        
        let queue = [this.root]
        console.log(queue)
        var result = [];
        while (queue.length != 0) {
            var node = queue.shift();
            result.push(node.val)
            if (node.left) {
                queue.push(node.left)
            }
            if (node.right) {
                queue.push(node.right)
            }




        }
        return result;
    }



}

var tr = new Tree();
tr.insert('A')
tr.insert('B', 'A', 'left')
tr.insert('C', 'A', 'right')
tr.insert('D', 'B', 'left')
tr.insert('E', 'B', 'right')
tr.insert('F', 'C', 'left')
tr.insert('G', 'C', 'right')

var DFS = tr.DFS();
console.log('DFS path is ', DFS.join(' => '))
var BFS = tr.BFS();
console.log('BFS path is ', BFS.join(' => '))