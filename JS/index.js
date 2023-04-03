const fs = require('fs')



// fs.writeFile('./testFile.txt', 'This is working in JS, but it requires far too much set up to be useful! \n', err => {
//     if (err) console.log(err)
//     console.log('Saved, check the file!')
// })

fs.appendFile('aNewFile.txt', ('Need to replace this with a user input method of some sort, but this is the default message') + '\n', (err) => {
    if(err) console.log(err)
    console.log('File has been created and something has been written in it, go see!')
})

// fs.open('./aNewFile.txt', (err, file) => {
//     if (err) console.log(err)
//     console.log('It has been opened!')
// })