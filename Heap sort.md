# 快速排序

## 排序原理

首先基于输入数组构造一个二叉树（建树），二叉树的元素由数组的元素按索引顺序从上到下、从左到右填入，具体实现方式就是给数组每个索引建立左子节点、右子节点及父节点的映射；然后调整数组的顺序使堆满足最大堆的性质，这一过程被称为建堆，建堆的方法有很多种；最后从最后一个节点开始，直至第二个节点，将其与第一个节点（也就是具有最大值的节点）交换，并重新调整交换之后的堆，使之满足最大堆的性质。

## 演示

**建树**
![建树](https://ws1.sinaimg.cn/large/005NHEMFly1g5ntpmeqgbj30gl06b3yt.jpg)
**建堆**
![建堆](https://ws1.sinaimg.cn/large/005NHEMFly1g5ntmuu7dmj30in0j5jt6.jpg)
**排序**
![排序](https://ws1.sinaimg.cn/large/005NHEMFly1g5ntng12efj30l70jltaj.jpg)