//SPDX-License-Identifier: MIT

pragma solidity >=0.6.0 <0.9.0;

contract SimpleStorage {
    // this will get initialized to 0!
    uint256 favoriteNumber;

    struct People {
        uint256 favoriteNumber;
        string name;
    }

    People[] public people;
    mapping(string => uint256) public nameToFavoriteNumber;

    function store(uint256 _favoriteNumber) public returns (uint256) {
        favoriteNumber = _favoriteNumber;
        return favoriteNumber;
    }

    // view: we only look at a information on the blockchain without changing it, pure: we only perform (mathematical) operations
    function retrieve() public view returns (uint256) {
        return favoriteNumber;
    }

    // The memory keyword means that the variable will only be stored for the execution of the function.
    // Using the keyword "storage" instead means that it will be stored even after the execution of the function.
    // The data type string is technically a type of an array of bytes, wherefore it requires one of these keywords.
    function addPerson(string memory _name, uint256 _favoriteNumber) public {
        people.push(People({name: _name, favoriteNumber: _favoriteNumber}));
        nameToFavoriteNumber[_name] = _favoriteNumber;
    }
}
