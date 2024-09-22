$date=(Get-Date).AddDays(-90)
$path="C:\data\"
$for_archived=Get-ChildItem -Path $path -Attributes d | where {$_.CreationTime -le $date} 

#Get-ChildItem -Path $path | where {$_.CreationTime -gt $date} | Compress-Archive -CompressionLevel="Optimal"

foreach ($file in $for_archived)
{
Compress-Archive -CompressionLevel "Optimal" -Path $path\$file -DestinationPath $path\$file".zip" -WhatIf
Remove-Item $path\$file -Recurse -WhatIf
}
