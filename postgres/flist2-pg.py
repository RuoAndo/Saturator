import sys 
import psycopg2

argvs = sys.argv  
argc = len(argvs) 

f = open(argvs[1])
software_version = argvs[2]

array = []
counter = 0

conn = psycopg2.connect(
    host = "192.168.1.1",
    port = 5432,
    database="sample",
    user="postgres",
    password="")

cur = conn.cursor()

sql = "drop TABLE definition;"
cur.execute(sql)

sql = "create TABLE test(id INT, software_version varchar(1024), type varchar(1024), function_type varchar(1024), function_name varchar(1024), location varchar(1024), linenumber INT);"
cur.execute(sql)

line = f.readline() 

counter = 0

while line:

    print "-------------"

    print line

    if line.find('(') > -1 and line.find(')') > -1:

        try:
            #uint64_t vhash(unsigned char m[],vmac_ctx_t *ctx):xen/crypto/vmac.c:846
            #uint64_t vmac(unsigned char m[],vmac_ctx_t *ctx):xen/crypto/vmac.c:951

            print line

            tmp = line.split("(")
            tmp3 = line.split(":")

            tmp21 = tmp[0].split(":")
            tmp2 = tmp21[1].split()
            
            function_type = ""
            for num in range(0, len(tmp2)-1):
                #print "   " + tmp2[num]
                function_type = function_type + " " + str(tmp2[num])

            function_name = tmp2[-1]
            print "function_name:" + function_name
            print "function_type:" + function_type
       
            tmp4 = tmp[1].split(")")
            print "arguments:" + tmp4[0]
            arguments = tmp4[0]

            print "location:" + tmp3[2]
            location = tmp3[2]
            print "linenumber:" + tmp3[3]
            linenumber = int(tmp3[3].rstrip())

            ########
            print "#### function ####"
            print "software_version:" + software_version
            print "type:" + definition
            print "function_type:" + function_type.lstrip()
            print "function_name:" + function_name
            print "location:" + location
            print "linenumber:" + linenumber
            print "####  #### ### ###"


            #sql = "create TABLE test(id INT, software_version varchar(1024), type varchar(1024), function_type varchar(1024), function_name varchar(1024), location varchar(1024), linenumber INT);"
            
            sql = "INSERT INTO test (id, software_version, type, function_type, function_name, location, linenumber) VALUES (" + str(counter) + ", '" + software_version + "', '" + type + "', '" + function_name + "', '" + location + "', '" + linenumber +"');"
            cur.execute(sql)
            
            #print "argument_type:" + arg_type

            # splitting arguments
            arg_tmp = tmp4[0].split(",")
            print arg_tmp
            for i in arg_tmp:
                arg_tmp_2 = i.lstrip()
                arg_tmp_3 = arg_tmp_2.split(" ")
                arg_type = ""
                for num in range(0, len(arg_tmp_3)-1):
                    arg_type = arg_type + " " + str(arg_tmp_3[num])
                    
                print arg_type + ":" + arg_tmp_3[-1]

                #collect.insert( { 'software_version' : software_version, 'type' : "definition", 'function_type' : function_type.lstrip(), 'function_name' :  function_name, 'location' : location, 'linenumber' : linenumber, 'argument_type' : arg_type, 'argment_name' : arg_tmp_3[-1], 'line' : line } )

        except:
            pass

    counter = counter + 1
    line = f.readline() 
