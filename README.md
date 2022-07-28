
<h1 align="left">使用本工具需要在Actions secrets添加3个secrets</h1>
<h2 align="left">1、WEB3_STORAGE_TOKEN这个是从web3.storage获得的 <br>2、DB_CONNECT数据库的远程链接字符串用的是mongodb.可以用官方免费的500m数据库，只使用Actions上传的话不需要<br/>3、SYNC_TOPIC (可选)下载完成功mqtt通知主题。客户端订阅该主题即可接收下载完成提示。</h2>
<h1>演示视频: <br><a href="https://youtu.be/A7pImBMentI" targe="_blank">https://youtu.be/A7pImBMentI</a> <br><a href="https://youtu.be/fqHjkzwPw_o" targe="_blank">https://youtu.be/fqHjkzwPw_o</a>
</h1>
<p>已经完全采用mongodb数据库的方法来处理下载地址的获取，请忽略视频中的url修改。<br/>
数据库中建立task表添加url和isnow字段.立即下载isnow=1,日常任务isnow=0
</p>


<p align="left">加入下载完成通知功能：利用免费的mqtt服务器:broker-cn.emqx.io实现下载完成后发送完成信息。需要在secrets里添加SYNC_TOPIC做为唯一订阅主题即可。本地随意处理。</p>


<p align="left">加入任务模式：不需要修改url内容，需要在mongodb内建立task表,插入url字段数据即可。每次查询一条url然后下载，查询后不管下载成功与否随即删除。对应actions为Download task.目前为手动触发。根据自己情况修改actions的触发为schedule即可。</p>

<h1 align="center">⁂<br/>web3.storage</h1>
<p align="center">Add a directory to web3.storage from an Action, and output it's IPFS Content ID.</p>


## Example usage

```yaml
uses: ykxVK8yL5L/add-to-web3@v1.3
id: web3
with:
  web3_token: ${{ secrets.WEB3_STORAGE_TOKEN }}
  path_to_add: 'dist'
  file_name:  'test'

# "bafkreicysg23kiwv34eg2d7qweipxwosdo2py4ldv42nbauguluen5v6am"
- run: echo ${{ steps.web3.outputs.cid }}

# "https://dweb.link/ipfs/bafkreicysg23kiwv34eg2d7qweipxwosdo2py4ldv42nbauguluen5v6am"
- run: echo ${{ steps.web3.outputs.url }}
```

## Inputs

### `path_to_add`

**Required** The path the root directory of your static website or other content that you want to publish to IPFS.

### `file_name`

**Required** file name that you want to publish to IPFS.



### `web3_token`

**Required** API token for web3.storage


<details>
  <summary>Show advanced input options</summary>


### `web3_api`

Useful for testing against dev deployments.
  
_Default_ `https://api.web3.storage`
  
### `wrap_with_directory`

Should the `path_to_add` be wrapped in a diretory when creating the IPFS DAG. For most folks using this, the default of `false` is fine. If you want to add a single file and preserve the filename in the IPFS DAG you may want to set it to `true`.'
  
_Default_ `false`


</details>

## Outputs

### `cid`

The IPFS content ID for the directory on IPFS. 
e.g. `bafkreicysg23kiwv34eg2d7qweipxwosdo2py4ldv42nbauguluen5v6am`

### `url`

The IPFS gateway URL for the directory 
e.g. `https://dweb.link/ipfs/bafkreicysg23kiwv34eg2d7qweipxwosdo2py4ldv42nbauguluen5v6am`


## Contibuting

💌 Considerate contributions welcome! 

*Of note* This is supposed to be a Javascript flavour GitHub Action, but the JS runner is [stuck on node12](https://github.com/actions/runner/issues/772v), and we need at least node14. Until the glorious future where the current node version is supported, we wrap the action in a container.

The `dist` folder is commited to the repo as is the curious cultural norm with JS actions, as the repo is the delivery mechanism, so to spare some cycles for the user users, all the deps are bundled into a single /dist/index.js monolith. This no longer makes much sense as we're also wrapping it in a container, but the dream is that the new node16 runner lands, and we can just delete the Dockers and move on.

<h3 align="center"><a href="https://web3.storage">⁂</a></h3>
