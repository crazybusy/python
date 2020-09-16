from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from datetime import datetime

def getpercentfin():
    try:        
# rpc_user and rpc_password are set in the bitcoin.conf file
        rpc_connection = AuthServiceProxy("http://%s:%s@%s:8332"%("user", "user", "192.168.2.100"))
        best_block_hash = rpc_connection.getblockchaininfo()
        
        if round(best_block_hash["blocks"]/best_block_hash["headers"]*100,2)== 100:
            mineblock(rpc_connection.getblocktemplate())
    except JSONRPCException:
        print ("You can't divide by zero, you're silly.")
    return

def mineblock(blocktemplate):
    print(blocktemplate)

if __name__ == "__main__":
    getpercentfin()

    input()
