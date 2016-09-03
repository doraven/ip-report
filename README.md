# ip-report
To solve the problem of dynamic ip.

I've bought an domain name in aliyun, directed to my computer at home.
 Problem is that ip of ChinaNet in this little country is dynamic.There're
 both advantages and disadvans.Good thing is that I don't need to report my
 site to the government.On the other hand, I need to write a script to get
 me known my ip has been changed.


## Solutions
- use python to get ip and email the newest ip to me.
    Of course, there are some details.such as:
    - can't get to internet right now
    - ip has not been changed
    ...
- use crontab of ubuntu to run this python script every 10 mins.
