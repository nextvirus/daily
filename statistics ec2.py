import boto3
import pandas as pd
import datetime
instanceid=[]
platform=[]
Name=[]
image=[]
vpc=[]
sub=[]
key=[]
RI=[]
role=[]
instancetype=[]
privateip=[]
publicip=[]
time=[]
ec2 = boto3.resource('ec2')
id = ec2.instances.all()
for i in id:
    instanceid.append(i.id)
    tag = ec2.Instance(i.id)
    for j in tag.tags:
        if j['Key']=='Name':
            Name.append(j['Value'])
    image.append(tag.image.id)
    vpc.append(tag.vpc_id)
    sub.append(tag.subnet_id)
    key.append(tag.key_name)
    privateip.append(tag.private_ip_address)
    publicip.append(tag.public_ip_address)
    instancetype.append(tag.instance_type)
    if tag.iam_instance_profile != None:
        role.append(tag.iam_instance_profile['Arn'].split('/')[1])
    else:
        role.append(tag.iam_instance_profile)
    if tag.platform == None:
        platform.append('Linux')
    else:
        platform.append(tag.platform)
    time.append(tag.launch_time.strftime('%Y-%m-%d %H:%M:%S')+'UTC')
    RI.append(tag.capacity_reservation_id)

dfData = { 
    '':'',
    'Name': Name,
    '实例id':instanceid,
    '实例类型':instancetype,
    'IPV4 公有地址':publicip,
    '密钥名称':key,
    '启动时间':time,
    'VPC ID':vpc,
    '子网 ID':sub,
    'IAM实例配置文件名称':role,
    '映像 ID':image,
    '平台':platform,
    'IPV4 私有地址':privateip,
    'RI':RI
}
df = pd.DataFrame(dfData)  # 创建DataFrame
df.to_excel('/Users/zhangshihao/work/daily/ec2实例统计.xlsx', index=False) ##记的修改excel保存路径


