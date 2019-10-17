# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs help` - Print this help message.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.



堆是具有以下性质的**完全二叉树**（尽左边放）：
>1. 每个结点的值都大于或等于其左右孩子结点的值，称为**大顶堆**；
>2. 或者每个结点的值都小于或等于其左右孩子结点的值，称为**小顶堆**。
>3. **跟结点**一定是**大顶堆中的最大值**，一定是**小顶堆中的最小值**；
![大顶堆与小顶堆](https://upload-images.jianshu.io/upload_images/7058492-3014930d87c6c744.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


用**简单的公式来描述一下堆的定义**就是：
>**大顶堆**：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]  
>**小顶堆**：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]  


####堆排序的基本思想

将待排序序列构造成一个大顶堆，此时，整个序列的最大值就是堆顶的根节点。将其与末尾元素进行交换，此时末尾就为最大值。然后将剩余n-1个元素重新构造成一个堆，这样会得到n个元素的次小值。如此反复执行，便能得到一个有序序列了


























