from fabric import Connection


class SSHconnection:
    def __init__(self,host,user,password,port=22):
        self.host = host   
        self.user =user              
        self.port =port                    
        self.password =password          


        self.conn = Connection(
            host=self.host, 
            user=self.user, 
            port=self.port, 
            connect_kwargs={"password": self.password})

    def executecommand(self,command):
        result = self.conn.run(command, hide=True)
        output=result.stdout.strip()
        
        print("Server response:\n", output)
        return str(output)
