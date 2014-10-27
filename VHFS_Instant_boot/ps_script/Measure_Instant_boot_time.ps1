#*******************************************************************************
# File Name :: InstantBoot.ps1
# Purpose   :: Script to create virtual machine in Hyper-V manager and attaching 
#              vhd files and start the virtual machine and open Console window and calculate booting time
# Author    :: priya
# Date      :: Wed 8 Oct 2014 
#*******************************************************************************


#Setting execution policies to run powershell scripts
set-executionpolicy -scope LocalMachine -executionPolicy Undefined -force
set-executionpolicy -scope CurrentUser -executionPolicy Undefined -force
set-executionpolicy -scope LocalMachine -executionPolicy AllSigned -force
set-executionpolicy -scope CurrentUser -executionPolicy RemoteSigned -force


Import-Module Hyper-V
#Importing hyper-v module to work with hyper-v cmdlet
#Import-Module "C:\Program Files\modules\HyperV\HyperV.psd1"

#$VHFSDir = D:\techteam5\2003\15_10_2014_0110
$VHDDir = "C:\Program Files\Vembu\StoreGrid\1\vembu-pc\VHd-boot-wo-comp\07_11_2014_1045\1-500\1"
$VHFSDIr = "F:\vembu-pc\IB-Mayank\23_10_2014_0700"
$dwnld = "C:\nnn\vembu-pc\sin_dsk_mul_part_10OCT2014_02_33_25\sin_dsk_mul_part"
$VHD_name_list = "c:\list_of_vhd_files.txt"
$Heart_Beat = "C:\heart_beat_of_vm.txt"
$n = 0


# Select the vhd files

Get-ChildItem  $VHDDir -Recurse | where {$_.extension -eq ".vhd"} | foreach-object {$_.Fullname} | Out-File $VHD_name_list –width 1024

# Get all the vhd path

$lines = Get-Content -Path $VHD_name_list

# For each vhd path run hyper -v commands

foreach ($line in $lines)

{
    write-host $line
    New-VM –Name “Test_machine$n” –MemoryStartupBytes 2048MB –VHDPath $line
    write-host "AddedVM"
    #Start-Sleep -s 20
    ADD-VMNetworkAdapter -vmname “Test_machine$n” -switchname "Switch1" -StaticMacAddress "00:30:12:11:48:11"
    Write-Host "AddedAdapter"
    #Start-Sleep -Seconds 30
    $starttime = Get-Date
    Start-VM –Name “Test_machine$n”
    Write-Host "StartedVM"
    Start-Sleep -Milliseconds 100
    #Disable-VMIntegrationService –Name Heartbeat -VMName Test_machine$n
    #Write-Host "Disable Integration Services"
    #Start-Sleep -s 10
    #Enable-VMIntegrationService –Name Guest Service Interface -VMName Test_machine$n
    #Write-Host "Enabled Integration Services"
    #Start-Sleep -s 10
    $bool = "true"
    $count = 1
    $do = 0
    
<#    while($bool -eq "true")

    {
	    Write-Host "inside while loop"
        #Get-VMIntegrationService -VMName “Test_machine$n” -Name Heartbeat | Out-File $Heart_Beat -Append
        ping -n 1 192.168.103.102 | Select-String "Reply" -quiet 
        #Write-Host "pinging" 
	    #$content = Get-Content $Heart_Beat
	    #$result = Get-Content $Heart_Beat | Select-String "ok" -quiet
        Write-Host "searched heartbeat"
	    if($result -eq "True")
	    {
	         $bool = "false" 
	         write-host $bool
             
    	}	
	    else
	    {
	        write-host "in else $count "
            Start-Sleep -s 2
	        $count = $count + 1
	        if($count -eq 500)
		    {
		         break
	   	    }
    	}
    } #>

    do 
    {
    Write-Host $do
    Start-Sleep -Milliseconds 100
    $do = $do + 1
    }Until(ping -n 1 192.168.103.28 | Select-String "TTL=" -quiet)
   
    $endtime = Get-Date
    write-host $starttime is start time
    write-host $endtime is end time

    $duration = (NEW-TIMESPAN –Start $starttime –End $endtime).TotalSeconds
    #$duration = $starttime - $endtime
    Write-Host $duration
    Add-Content C:\Output_Boot_time.txt "$n $duration"

    <# $secpasswd = ConvertTo-SecureString "Tech123$" -AsPlainText -Force
    $mycreds = New-Object System.Management.Automation.PSCredential("Administrator", $secpasswd)
    New-SSHSession -ComputerName "192.168.103.28" -KeepAliveInterval 10000 -Credential $mycreds -verbose
    #Invoke-SSHCommand -Index 0 -Command "ipconfig;" -verbose
    Invoke-SSHCommand -Index 0 -Command "cd c:/;C:/DataTransferTest.exe" -EnsureConnection -verbose >> C:\Output_Boot_time.txt
    Remove-SSHSession -Index 0 -Verbose #>

    Start-Sleep -s 5
    Stop-VM –Name “Test_machine$n”  -force -confirm:$false
    Start-Sleep -s 50
    Remove-VM –Name “Test_machine$n” -force -confirm:$false
    Start-Sleep -s 5

    #Remove-Item $Heart_Beat
    Write-Host $line completed
    $n = $n + 1
}