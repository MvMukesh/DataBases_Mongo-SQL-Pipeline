# Getting Data From Multiple Tables using `Joins` and `Subquery`(query within a query)
`Covered`
* Joins there types & application by joining two table
    * Self join 
* Subquery
---
`Overview`
* Joins => Clause, helps retrive data from multiple tables ![image](https://user-images.githubusercontent.com/26667491/127117631-e2848c5f-11db-4d59-81c1-8b84780b8642.png) ![image](https://user-images.githubusercontent.com/26667491/127117893-4a09d8be-aee0-4e16-bfb1-240599748127.png)
`Objective`   
* To get name of all users who have applied for job_id 2
* There salary, current designaition along with job_degisnation and hiring company they applied to ![image](https://user-images.githubusercontent.com/26667491/127119897-a3099847-fd9d-4122-b08c-fbe423b45dfd.png)

`Types of joins` with uses stats => ![image](https://user-images.githubusercontent.com/26667491/127125822-98ed0657-0244-4060-b982-2052b9974121.png)
![image](https://user-images.githubusercontent.com/26667491/127126270-cc16ef8a-9a6e-4cd4-a98e-2b586008abcc.png)
* `Left join` Takes all record from left table and only matching or corresponding record from right table
* `Key` same matching columns in both tables on which data is being matched

`Left join application Example` used 99% of time
* `To find Phone number/name of users who atleast have done one purchase/active user?`
![image](https://user-images.githubusercontent.com/26667491/127127085-c0802aee-65ee-4673-a572-e3f3662d637a.png)
* `User ID field is common key in both table`
* Putting Purchase table in left as hunt is for details of users/customers who ever did purchase any stuff and Contact Detail on right, perform a left join
`Query` => `select ContactDetails.Name, ContactDetails.PhoneNumber from Purchases left join ContactDetails on Purchases.UserID = ContactDetails.UserID`
* `NOTE:` 
   * Key name nead not to be same all time
   * target table must be put at left most in all situation as only data of leftmost table is required
   * Concept of join is not for only two table
   * Final result can also be joined to another table

* `Inner join` Used appx 9% of time in application

![image](https://user-images.githubusercontent.com/26667491/127129616-95e3b54b-e304-471c-84da-a56588b16b04.png)

* `Cartesian/Cross join` rare use

![image](https://user-images.githubusercontent.com/26667491/127130016-1e66ff65-85ef-47a5-9a04-9e2c02baed21.png)

* `Right join` rare use

![image](https://user-images.githubusercontent.com/26667491/127130194-cc335cf5-370b-4c79-95c8-b6e8ef4d8ca8.png)

* `Self join` 

![image](https://user-images.githubusercontent.com/26667491/127130538-691c1f86-625b-4213-91aa-7fe61ca6ecf0.png)
   * join of 2 copies of same table 

