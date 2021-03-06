# This code calculat Network ID, first and last host IPV4, Broadcast IP
# Give user either to enter Netword ID along with CIDR or long format mask
# Also convert long format mask eg 255.255.255.252 into prifix(CIDR) /30

def choice():
    print("\n********  choice ******: " )
    operation = {   1:"Enter Network ID with CIDR, eg 10.2.2.88/27 ** ",
                    2:"If you want to enter Network ID without CIDR, eg 10.2.2.88 255.255.255.224 **   ",
                    3:"To convert long format mask to corresponding CIDR, eg 255.255.255.244 to /27 ** " } 
         
    for key in operation:
            print(key,":-" , operation[key] )
    user_choice = int(input("Please choose one from 1 - 3: "))
    if user_choice not in operation:
        not_valid = True 
        while not_valid:
            user_choice = int(input("invalid choice, Please choose one from 1 - 3:  "))
            if user_choice in operation:
                not_valid = False
    return user_choice

#return number of 255 occurance eg take 255.255.224.0 and return 2
# It indicates target octet should increament  
def mask_priff(long_mask):
    for x in range((len(long_mask))):
        if (long_mask[x]) != 255:
            if (long_mask[x] != 0):   
                return x 
            else:
                return x - 1


#take network id and 
def calculat_prefix():
    long_mask= input("Please enter long daciaml format mask: eg 255.255.255.224 *** ").split(".")
    long_mask = [int(x) for x in long_mask]
    num_255 =  mask_priff(long_mask)
    inital = 128
    x = inital
    coun = 1
    prefix = (8 * num_255) 
    target_octet = long_mask[num_255]
    if target_octet != inital:
        for i in range(8):
            coun += 1
            x /= 2 
            inital = int(x) + inital
            if target_octet == inital:
                prefix = (coun  + prefix )
                return prefix
    elif target_octet == 0:
        return print
    else:
        prefix = coun  + prefix 
        return prefix     

#print back user inpute
def class_identi(network_id):
    for x in range(len(network_id)):
        print(network_id[x], end=".")

#calculate usable host it takes given cidr to find borrowed bit's 
def usable_host(given_cider):
    # off bits(zero's)
    off_bits = (32 - given_cider)
    host = (2 ** off_bits) - 2
    return host

#indicat target octet eg if cidr 21, ID 10.2.34.88 target octet is in index 2 which is 34
def octet(given_cid):
    return given_cid // 8 

#return default cidr
def default_cidr(ip_add):
    if(ip_add[0] >= 1 and ip_add[0] <= 127):
        return 8
    elif(ip_add[0] >= 128 and ip_add[0] <= 191):
        return 16
    elif(ip_add[0] >= 192 and ip_add[0] <= 223):
        return 24
    else:
        return 32
#indicate block size
def majic_num_indicater(giv_cidr,def_cidr):
    borrowed_bit = (giv_cidr) - (def_cidr)
    if borrowed_bit > 8:
        return borrowed_bit % 8
    else:
        return borrowed_bit

#subnet in the network
def subnet(giv_cidr, def_cidr):
    borrowed_bits = (giv_cidr) - (def_cidr)
    return 2 ** borrowed_bits

#  
def block_size(blo_si_indi):
    maj_num = 1
    y = (8 - blo_si_indi) 
    for x in range(y):
        maj_num += maj_num
    return maj_num

def class_type(defa_cidr):
    class_identi(ip_add)
    #defa_cidr = default_cidr(ip_add)
    print("\n||=====================|=====================")
    print(f"|| given CIDR          | /{cidr} " )
    if defa_cidr == 8:
        print(f"|| Class A default     | /{defa_cidr} CIDR ")
    elif defa_cidr == 16:
        print(f"|| Class B default     | /{defa_cidr} CIDR ")
    elif defa_cidr == 24:
        print(f"|| Class C default     | /{defa_cidr} CIDR ")
    else:
        print(f"|| Class D default     | /{defa_cidr} CIDR ")

def operation():
    #defa_cidr = default_cidr(ip_add)
    #get default cider and class type
    class_type(defa_cidr)
    usable_host(cidr)
    octet_pos = octet(cidr)
    subnet(cidr, defa_cidr)
    block_si = majic_num_indicater(cidr,defa_cidr)
    network_block_size = block_size(block_si)
    ip_add[octet_pos]
    show_result()
    
def show_result():
    print(f"|| Total subnet:-      | {subnet(cidr, defa_cidr)} ")
    #print(f"<<== Octat need to incremaent in {(octet_pos + 1)}")
    #print(f"<<== Target octat valu :- {ip_add[octet_pos]}")
    print(f"|| Block size:-        | {network_block_size} ")
    print(f"|| Total usable host:  | {usable_host(cidr)}")

    if  ip_add[octet_pos] > (network_block_size):
        divis = ip_add[octet_pos] //   network_block_size
        ip_add[octet_pos] = (divis *  network_block_size)
        if ip_add[octet_pos] > 255:
           ip_add[octet_pos - 1] += 1
           ip_add[octet_pos] = 0
        print("|| Network ID:-        |",*ip_add, sep=".")
        ip_add[octet_pos] += 1 
        print("|| First Host IP:-     |",*ip_add, sep=".")
        ip_add[octet_pos] += (network_block_size - 3)
        print("|| Last Host IP:-      |",*ip_add, sep=".")
        ip_add[octet_pos] += 1 
        print("|| Broadcast IP:-      |",*ip_add, sep=".")
        ip_add[octet_pos] += 1
        print("|| Next Subnet:-       |",*ip_add, sep=".")

    elif  ip_add[octet_pos] == (network_block_size):
        if (ip_add[octet_pos] > 255):
            ip_add[octet_pos - 1] += 1
            ip_add[octet_pos] = 0
        print("|| Network ID:-        |",*ip_add, sep=".")
        ip_add[octet_pos] += 1
        print("|| First Host IP:-     |",*ip_add, sep=".")
        ip_add[octet_pos] += (network_block_size) 
        print("|| Last Host IP:-      |",*ip_add, sep=".")
        ip_add[octet_pos] += 1
        print("|| Broadcast IP:-      |",*ip_add, sep=".")
        ip_add[octet_pos] += 1
        print("||  Next Subnet:-      |",*ip_add, sep=".")

    else:
        ip_add[octet_pos] = 0
        print("|| Network ID:-        |",*ip_add, sep=".")
        ip_add[octet_pos] += 1
        print("|| First Host IP:-     |",*ip_add, sep=".")
        ip_add[octet_pos] += (network_block_size - 3) 
        print("|| Last Host IP:-      |",*ip_add, sep=".")
        ip_add[octet_pos] += 1
        print("|| Broadcast IP:-      |",*ip_add, sep=".")
        ip_add[octet_pos] += 1
        print("|| Next Subnet:-       |",*ip_add, sep=".")


choice = choice()
   
if choice == 1:
#print(type(cidr_default))
    ip_add = (input("Enter IP address with CIDR, eg 10.2.2.88/27 *** ")).split(".")
    find_cidr = (ip_add[3]).split("/")
    find_cidr = [int(i) for i in find_cidr]
    cidr = find_cidr[1]
    ip_add[3] = (find_cidr[0])
    ip_add = [int(i) for i in ip_add]
    #get default cider and class type
    defa_cidr = default_cidr(ip_add)
    class_type(defa_cidr)
    usable_host(cidr)
    octet_pos = octet(cidr)
    subnet(cidr, defa_cidr)
    block_si = majic_num_indicater(cidr,defa_cidr)
    network_block_size = block_size(block_si)
    ip_add[octet_pos]
    show_result()
      
elif choice == 2:
    ip_add = (input("Enter IP address without CIDR, eg 10.2.2.88 *** ")).split(".")
    ip_add = [int(i) for i in ip_add]
    cidr = calculat_prefix()
    defa_cidr = default_cidr(ip_add)
    class_type(defa_cidr)
    usable_host(cidr)
    octet_pos = octet(cidr)
    subnet(cidr, defa_cidr)
    block_si = majic_num_indicater(cidr,defa_cidr)
    network_block_size = block_size(block_si)
    ip_add[octet_pos]
    show_result()
    
elif choice == 3:
    print("\nThe corrosponding CIDR is /",calculat_prefix())
else:
    pass
#response = input("Would you like to calculate network ID again?:  Y/N: ").lower()
#if response == "n":
    #print("Good bye!!")
    #quit()
 
       