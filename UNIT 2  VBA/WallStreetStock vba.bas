Attribute VB_Name = "Module1"
'

Sub WallStreetStock()
' Create a script that will loop through one year of stock data for each run and return the total volume each stock had over that year.
' You will also need to display the ticker symbol to coincide with the total stock volume.
' Your result should look as follows (note: all solution images are for 2015 data).

' Set innitial variable
Dim total_volume_stock As Double
Dim ticker As String
' Define value at open and close
Dim value_open
Dim value_close
Dim difference_openclose
'Define vol and it strart value
Dim vol As Double
vol = 0
' Define the Summary Table
' Dim Summary_Table As Integer
' Define the number of Row in the Summary Table
'Summary_Table = 4
'Print the header of the column I and J
Cells(1, 9).Value = "Ticker"
Cells(1, 10).Value = "Total Stock Vol"

' Loop to check within the stock value
For i = 2 To 705714

If value_open = 0 Then
value_open = Cells(i, 3).Value
 End If

If (Cells(i + 1, 1).Value <> Cells(i, 1).Value) Then
  ticker = Cells(i, 1).Value
  vol = Cells(i, 7).Value
  vol = 0
'create ticker
value_open = Cells(i, 3).Value
value_close = Cells(i, 6).Value

difference_openclose = value_close - value_open
Else
    vol = vol + Cells(i, 7).Value

End If
Next i

End Sub

