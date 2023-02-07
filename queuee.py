customer_no = 8
customers = [i for i in range(customer_no)]

IAtime = [0, 0, 4, 2, 0, 15, 2, 3]
service_time = [2, 5, 4, 1, 3, 2, 4, 1]
arrival_time = [sum(IAtime[0:i+1]) for i in range(len(IAtime))]
service_end = [0 for i in range(len(customers)+1)]
service_begin = [0 for i in range(len(customers))]
Time_Customer_Waiting_in_Queue = [0 for i in range(len(customers))]
Time_Customer_Spend_in_System = [0 for i in range(len(customers))]
System_idle = [0 for i in range(len(customers))]


for i in range(len(customers)):
    service_begin[i] = max(service_end[i-1], arrival_time[i])
    service_end[i] = service_begin[i]+ service_time[i]
    Time_Customer_Waiting_in_Queue[i] = service_begin[i]-arrival_time[i]
    Time_Customer_Spend_in_System[i] = service_end[i] - arrival_time[i]
    
System_idle = [max(0,arrival_time[i]-service_end[i-1]) for i in range(len(customers))]
service_end.pop()

no_customer_who_are_waiting = len(list(filter(lambda x:x>0,Time_Customer_Waiting_in_Queue)))
server_busy_time = 1 - sum(System_idle) / service_end[-1]  
W = sum(Time_Customer_Spend_in_System)/len(customers)
Wq = sum(Time_Customer_Waiting_in_Queue)/len(customers)

stack = [0 for i in range(service_end[-1])]
for i in range(service_end[-1]):
    for j in range(len(customers)):
        if (i in range(arrival_time[j],service_end[j])):
           stack[i]+=1


T = [stack.count(i) for i in range(no_customer_who_are_waiting)]
L = sum([i*T[i] for i in range(len(T))])/service_end[-1]

Tq = [T[i]+T[i+1] if i == 0 else T[i+1] for i in range(len(T)-1)]
Lq = sum([i*T[i] for i in range(len(Tq))])/service_end[-1]
 
print("\n")
print(f"Customers\tInter-Arrival Time\tService Time\tService Begin\tService End")

for i in range(len(customers)):
    print(f'{i+1:<9d} \t {IAtime[i]:<18d} \t {service_time[i]:<12d} \t {service_begin[i]:<13d} \t {service_end[i]:<11d}')
print("\n")

print(f"Long run time avg. no. of customers in system \t\t[L]\t: {L:.4f}")
print(f"Long run time avg. no. of customers in queue \t\t[LQ]\t: {Lq:.4f}")
print(f"Long run avg. time spent in the system per customer \t[W]\t: {W:.4f}")
print(f"Long run avg. time spent in the queue per customer \t[WQ]\t: {Wq:.4f}")
print(f"Server Utilization\t\t\t\t\t[%]\t: {server_busy_time*100:.2f}%")