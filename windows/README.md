# SSH Problem using VSCode

- When using Remote-SSH module in VSCode, you might get an error. 

```
Bad owner or permissions on C:\\Users\\gus/.ssh/config
```

- Under same condition, connecting through other SSH tool (MobaXterm) might work.
- However, `.ssh/config` file that VSCode generates is what causes the problem.
- I have tried many solutions suggested by various links, such as
  - https://github.com/Microsoft/vscode-remote-release/issues/119
- but nothing seemed to works using solutions like
  - changing the Security Settings for `config` file, or
  - updating the ssh settings through commands using powershell.
  
## I solved the problem through following steps

  1. assume that a public key(rsa_id.pub) is stored properly in the server(Ubuntu) side's `~/.ssh/authorized_keys`, and that OpenSSH Client is installed on the client(Windows)
  2. delete the `.ssh` folder in the client(Windows) side
  3. try connecting the server using `ssh` command in powershell, which will create a `.ssh` folder for you
  ```
  ssh server_user_name@server_ip
  ``` 
  4. copy the private key(rsa_id) in the newly created `.ssh` folder
  5. when writing the config file in VSCode, instead of using problematic `C:\Users\username\.ssh\config` file, wirte your configurations using `C:\ProgramData\ssh\ssh_config` 
    - note that you don't have to specify the path of your private key(rsa_id), which is user `.ssh`
  6. try connecting Remote-SSH again, which will work fine!
  
  - my sample `C:\ProgramData\ssh\ssh_config` 
```
# Read more about SSH config files: https://linux.die.net/man/5/ssh_config
Host ubuntu_host
  HostName 35.223.9.77
  User gus_an
```
- KEY POINT : delete `config` file in the `C:\Users\username\.ssh` directory!
