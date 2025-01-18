### Log vai jebkāda cita faila nolasīšana

3.rindiņā ir jāpievieno faila atrašanās vieta, testa failā ir pievienots teksts, kas izsktās kā log faila izdruka. 
Terminālī tiek izdrukāts timestamp un fiksētā ieraksta apraksts, piemērs:

```bash
[('Jan 15 10:24:30', 'usb 1-1: new high-speed USB device number 5 using xhci_hcd')]
[('Jan 15 10:24:31', 'usb 1-1: New USB device found, idVendor=0781, idProduct=5567')]
[('Jan 15 10:24:31', 'usb 1-1: New USB device strings: Mfr=1, Product=2, SerialNumber=3')]
[('Jan 15 10:25:15', 'usb 2-2: USB disconnect, device number 7')]
[('Jan 15 10:27:15', 'usb 3-4: new SuperSpeed USB device number 9 using xhci_hcd')]
[('Jan 15 10:27:15', 'usb 3-4: New USB device found, idVendor=046d, idProduct=082d')]
[('Jan 15 10:28:30', 'usb 1-1: USB device not accepting address 9, error -32')]
[('Jan 15 10:29:45', 'usb-storage 1-1:1.0: USB Mass Storage device detected')]
[('Jan 15 10:30:12', 'usb 1-2: USB suspend operation completed successfully')]
[('Jan 15 10:31:01', 'usb 2-3: USB resume completed')]
```