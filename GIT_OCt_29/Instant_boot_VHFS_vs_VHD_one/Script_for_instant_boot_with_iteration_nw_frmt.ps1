#*******************************************************************************
# File Name :: Script_for_instant_boot_with_iteration_nw_frmt.ps1
# Purpose   :: Script to calculate duration of instant boot of average 10 iteration
# Author    :: priya
# Date      :: Tue 28 Oct 2014 
#*******************************************************************************


#Setting execution policies to run powershell scripts
set-executionpolicy -scope LocalMachine -executionPolicy Undefined -force
set-executionpolicy -scope CurrentUser -executionPolicy Undefined -force
set-executionpolicy -scope LocalMachine -executionPolicy AllSigned -force
set-executionpolicy -scope CurrentUser -executionPolicy RemoteSigned -force

#Importing hyper-v module to work with hyper-v cmdlet
Import-Module Hyper-V

#VHD source location

$VHDDir = "D:\VHD_copy\1"
$Destination_folder = "D:\Destination_VHD_folder"
$text = "D:\text_1"
$count = 0
$dur = 0
$duration = 0

# Name list of all vhds in source location

$VHD_name_list = "D:\VHD_name_list.txt"
$VHD_Dest_list = "D:\VHD_Dest_list.txt"

# Select the vhd files

Get-ChildItem  $VHDDir -Recurse | where {$_.extension -eq ".vhd"} | foreach-object {$_.Fullname} | Sort-Object Length | Out-File $VHD_name_list –width 1024

for ($i=1; $i -le 11; $i++)
{
    $count = 0
    Write-host ("Inside main for loop of $i th incremental")
    $i_incrmental = Get-Content $VHD_name_list -TotalCount $i
    Write-Host ("Start copying the $i_incrmental files to destination")
    $s = Get-Date
    foreach ($incr in $i_incrmental)
    {
       
        
        Copy-Item $incr $Destination_folder
        Write-Host( "copied $incr")
        
    }

    $d = Get-Date
    $dur = (NEW-TIMESPAN –Start $s –End $d).TotalSeconds
    #$duration = $starttime - $endtime
    Write-Host ("time taken to copy the files $dur")

    Get-ChildItem  $Destination_folder -Recurse | where {$_.extension -eq ".vhd"} | foreach-object {$_.Fullname} | Sort-Object Length | Out-File $VHD_Dest_list –width 1024   
    $boot_file = Get-Content $VHD_Dest_list | Select -Index ($i - 1)
    Write-Host ($boot_file)
   
    while ($count -lt 2)
    {
        $do = 0
        Write-Host ("Create machine with this $boot_file file")
        New-VM –Name “Test_machine” –MemoryStartupBytes 2048MB –VHDPath $boot_file
        write-host "AddedVM"
        #Start-Sleep -s 20
        ADD-VMNetworkAdapter -vmname “Test_machine” -switchname "Switch1" -StaticMacAddress "00:30:12:11:48:11"
        Write-Host "AddedAdapter"
        #Start-Sleep -Seconds 30
        Write-Host ("Starting $boot_file this machine for $count time")
        $starttime = Get-Date
        Start-VM –Name “Test_machine”
        Write-Host "StartedVM"
        Start-Sleep -Milliseconds 100
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
        if ( $count -eq 0)
        {
            Write-Host ("Added content of first")
            Add-Content D:\Output_Boot_time_first.txt "$boot_file $duration"
        }
        else
        {
             Write-Host ("Added content of second")
            Add-Content D:\Output_Boot_time_Second.txt "$boot_file $duration"   
        }

        Start-Sleep -s 70
        Stop-VM –Name “Test_machine”  -force -confirm:$false
        Start-Sleep -s 20
        Remove-VM –Name “Test_machine” -force -confirm:$false
        Start-Sleep -s 5

        #Remove-Item $Heart_Beat
        #Write-Host $line completed
        $count = $count + 1
    }

    Remove-Item D:\Destination_VHD_folder\*
    Write-Host ("Removed files")
}


