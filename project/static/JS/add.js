console.log('JavScript Connected')
const form=document.querySelector('.form');
const name=document.getElementById('fullname');
const pan=document.getElementById('pan');
const email=document.getElementById('email');
const age=document.getElementById('age');
const gender=document.getElementById('gender');
const city=document.getElementById('city')


form.addEventListener('submit', (e)=>{
	console.log('Inside Event Listener')
	if(checkInputs()!==true)
	{
		e.preventDefault();
	}

})


function checkInputs()
{
	const nameValue=name.value.trim();
	const panValue=pan.value.trim();
	const emailValue=email.value.trim();
	const ageValue=age.value.trim();
	const genderValue=gender.value;
	const cityValue=city.value;

	if(isName(nameValue))
	{
		console.log('NAme')
		setSuccessFor(name)
		if(isPan(panValue))
			{
				setSuccessFor(pan);
				if(isEmail(emailValue))
					{
						setSuccessFor(email);
						console.log('email done')
						if(isAge(ageValue))
							{
								setSuccessFor(age);
								if(genderValue!=='')
									{
										setSuccessFor(gender);
										if(cityValue!=='')
											{
												setSuccessFor(city);
												console.log('Finally returning true')
												return true;
											}
											else
											{
												setErrorFor(city, 'Invalid EMail ID')
											}
									}
									else
									{
										setErrorFor(gender, 'Invalid EMail ID')
									}
								
							}
							else
							{
								setErrorFor(age, 'Invalid EMail ID');
								return false;
							}
					}
					else
					{
						setErrorFor(email, 'Invalid EMail ID')
						return false;
					}
			}
			else
			{
				setErrorFor(pan, 'Invalid PAN Number');
				return false;
			}
	
	}
	else
	{
		setErrorFor(name, 'Invalid Name')
		return false
		
	}

 
}


function setErrorFor(input, message){
	const formControl = input.parentElement;
	const small=formControl.querySelector('small');
	small.innerText=message;

	formControl.className='form-control error'

}

function setSuccessFor(input)
{
	const formControl = input.parentElement;
	formControl.className='form-control success'
}


function isEmail(emailValue) {
	var emailPattern=/\w+@[a-zA-Z]+\.[a-z]+$/;
	console.log('Email: '+emailPattern.test(emailValue));
	return emailPattern.test(emailValue);
}

function isName(name)
{
	var namePattern=/[A-Za-z\\s]+$/;
	console.log('Name: '+namePattern.test(name));
	return namePattern.test(name);
}

function isPan(panValue)
{
	var panPattern=/[a-zA-Z0-9]+$/;
	console.log('Pan: '+panPattern.test(panValue));
	return panPattern.test(panValue);
}

function isAge(ageValue)
{
	if (ageValue>=1 && ageValue<=100)
	{
		console.log('true');
		return true;
	}
	else
	{
		return false;
	}
}