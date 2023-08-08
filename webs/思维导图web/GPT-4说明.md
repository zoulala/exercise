
# 问：
> 写一个前端页面和js代码，通过接口获取一个json数据，并将数据以树状结构的思维导图展示


# GPT-4：
这里是一个简单的前端页面和相应的 JavaScript 代码，用于通过接口获取 JSON 数据并以树状结构的思维导图进行展示。假设接口 URL 是 `https://your-api-endpoint.com/data`，返回的 JSON 数据格式如下：

```json
{
  "name": "根节点",
  "children": [
    {
      "name": "节点1",
      "children": [
        {"name": "节点1.1"},
        {"name": "节点1.2"}
      ]
    },
    {
      "name": "节点2",
      "children": [
        {"name": "节点2.1"},
        {"name": "节点2.2"}
      ]
    }
  ]
}
```

**HTML 页面：**

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>树状思维导图示例</title>
  <style>
    /* 这里添加一些基本的样式 */
    .node {
      cursor: pointer;
    }

    .node circle {
      fill: #fff;
      stroke: steelblue;
      stroke-width: 3px;
    }

    .node text {
      font: 12px sans-serif;
    }

    .link {
      fill: none;
      stroke: #ccc;
      stroke-width: 2px;
    }
  </style>
</head>

<body>
  <script src="https://d3js.org/d3.v5.min.js"></script>
  <script>
    // 这里添加 JS 代码
  </script>
</body>

</html>
```

**JavaScript 代码：**

```javascript
(async () => {
  const response = await fetch('https://your-api-endpoint.com/data');
  const data = await response.json();

  // 创建 SVG
  const svg = d3.select('body')
    .append('svg')
    .attr('width', 960)
    .attr('height', 600)
    .append('g')
    .attr('transform', 'translate(40,0)');

  // 创建布局
  const treeLayout = d3.tree().size([500, 900]);

  // 创建层次结构
  const root = d3.hierarchy(data);
  treeLayout(root);

  // 绘制节点
  const nodes = svg.selectAll('.node')
    .data(root.descendants())
    .enter()
    .append('g')
    .attr('class', 'node')
    .attr('transform', d => `translate(${d.y},${d.x})`);

  nodes.append('circle')
    .attr('r', 10);

  nodes.append('text')
    .attr('dy', 3)
    .attr('x', d => d.children ? -15 : 15)
    .style('text-anchor', d => d.children ? 'end' : 'start')
    .text(d => d.data.name);

  // 绘制连接线
  const links = svg.selectAll('.link')
    .data(root.links())
    .enter()
    .append('path')
    .attr('class', 'link')
    .attr('d', d3.linkHorizontal()
      .x(d => d.y)
      .y(d => d.x)
    );
})();
```

这个示例使用 d3.js 来绘制树状图。首先，通过 fetch API 获取 JSON 数据，然后使用 d3.js 创建 SVG、布局和层次结构。最后，绘制节点和连接线以展示树状思维导图。