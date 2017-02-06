using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Key : MonoBehaviour 
{
    //Create a reference to the KeyPoofPrefab and Door
	public GameObject keyPoof;
	public GameObject door;

	void Update()
	{
		//Bonus: Key Animation
	}

	public void OnKeyClicked()
	{
        // Instatiate the KeyPoof Prefab where this key is located
		Instantiate (keyPoof, transform.position, Quaternion.Euler(270, 0, 0));

        // Inform Door that user possesses key before destroying the Key instance.
		Door.holdsKey = true;
//		Door.Unlock();

        // Destroy the key. Check the Unity documentation on how to use Destroy
		Destroy(gameObject);
    }

}
