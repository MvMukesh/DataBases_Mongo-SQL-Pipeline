# String Functions

* `Concat`
* ![image](https://user-images.githubusercontent.com/26667491/127139777-173934a6-8889-434d-bc80-85eb0d9b52c7.png)
  * concat player name and nationality ??
    * select `conacat(name, "||", nationality)` from players limit 5;

* `Case Conversion`
  * display nationality in upper/lower case of first n player ??
    * select `ucase(nationality)` from players limit 5; 
    * select `lcase(nationality)` from players limit 5; 

* `Trimming String` leading spaces => left sidespaces, trailing spaces => rigth side spaces
  * select `ltrim("   nationality")` from players limit 5;
  * select `rtrim("nationality    ")` from players limit 5; 
  * select `trim("   nationality    ")` from players limit 5;   =>trim from both side  

* `Slicing String/Extracting Substring` 
  * Find first_2/last_2/from_middle char of name of players ??
    * select `left(Name,2)` from players limit 5; 
    * select `right(Name,2)` from players limit 5;
    * select `substring(Name,2,5)` from players limit 5;
