import os, sys
import stat

def getPermissionResult(ur,uw,ux,gr,gw,gx,otr,otw,otx):
    permission = 0000
    if ur:
        permission = permission | stat.S_IRUSR
    if uw:
        permission = permission | stat.S_IWUSR
    if ux:
        permission = permission | stat.S_IXUSR
    if gr:
        permission = permission | stat.S_IRGRP
    if gw:
        permission = permission | stat.S_IWGRP
    if gx:
        permission = permission | stat.S_IXGRP
    if otr:
        permission = permission | stat.S_IROTH
    if otw:
        permission = permission | stat.S_IWOTH
    if otx:
        permission = permission | stat.S_IXOTH
                            
    return permission

def createDir(fullPath,ur,uw,ux,gr,gw,gx,otr,otw,otx):
    permission = getPermissionResult(ur,uw,ux,gr,gw,gx,otr,otw,otx)
    os.mkdir(fullPath,permission)
    if gw:          
        os.chmod(fullPath,permission | stat.S_IWGRP)   #cannot set 0775 permission using mkdir, it's changing to 0755
    if otw:
        os.chmod(fullPath,permission | stat.S_IWOTH)   #cannot set 0757 permission using mkdir, it's changing to 0755

def changePer(fullPath,ur,uw,ux,gr,gw,gx,otr,otw,otx):
    permission = getPermissionResult(ur,uw,ux,gr,gw,gx,otr,otw,otx)
    os.chmod(fullPath,permission)

def main():
    # default permission 
    d = 1   #create directory
    ur = 1
    uw = 1
    ux = 1
    gr = 1
    gw = 1
    gx = 1
    otr = 1
    otw = 1
    otx = 1
    name = "untitled"
    
    if(len(sys.argv) > 1):
        if(input("set user read permission? (y|n) ") == "n"):
            ur = 0
        if(input("set user write permission? (y|n) ") == "n"):
            uw = 0
        if(input("set user execute permission? (y|n) ") == "n"):
            ux = 0
        if(input("set group read permission? (y|n) ") == "n"):
            gr = 0
        if(input("set group write permission? (y|n) ") == "n"):
            gw = 0
        if(input("set group execute permission? (y|n) ") == "n"):
            gx = 0
        if(input("set other read permission? (y|n) ") == "n"):
            otr = 0
        if(input("set other write permission? (y|n) ") == "n"):
            otw = 0
        if(input("set other execute permission? (y|n) ") == "n"):
            otx = 0
    else:
        print("error-occured")
        sys.exit()

    if (sys.argv[1] == "-c"):
        if(len(sys.argv) == 3):
            fullPath = sys.argv[2]
            changePer(fullPath,ur,uw,ux,gr,gw,gx,otr,otw,otx)
        else:
            print("error-occured")
            sys.exit()            
    else:
        if(input("create a file or directory? (f|d) ") == "f"):
            d = 0
        name = input("input the name for file or directory : ")
        path = sys.argv[1]
        fullPath = os.path.join(path,name)
        if d:
            createDir(fullPath,ur,uw,ux,gr,gw,gx,otr,otw,otx)
        else:
            open(fullPath,"w+")
            changePer(fullPath,ur,uw,ux,gr,gw,gx,otr,otw,otx)    

if __name__ == "__main__":
    main()