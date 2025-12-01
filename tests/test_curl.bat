@echo off
echo Testing Question Answering API...
echo.

curl -X POST "http://localhost:5000/ask" ^
     -H "Content-Type: application/json" ^
     -d @test_payload.json

echo.
echo.
echo Test complete.
pause
