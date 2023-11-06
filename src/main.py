import nacos
import uvicorn
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from suds.client import Client
from suds.transport.https import HttpAuthenticated
 
client=nacos.NacosClient('172.16.244.200:8848',namespace='Public')
 
async def beat():
    client.add_naming_instance('fastapi-service','172.16.244.10',8000,group_name='dev')
    
 
# 微服务注册nacos
def register_nacos():
    client.add_naming_instance('fastapi-service','172.16.244.10',8000,group_name='dev')
 
 
app=FastAPI()
 
# 微服务注册
register_nacos()
 
 
@app.on_event('startup')
def init_scheduler():
 
    scheduler = AsyncIOScheduler(timezone="Asia/Shanghai")
    scheduler.add_job(beat, 'interval', seconds=5)
    scheduler.start()
 
@app.get('/sap/materials')
async def sap_materials():
    ''' 功能实现'''
    return JSONResponse({'code':1000,'msg':'succ','data':data},status_code=200)