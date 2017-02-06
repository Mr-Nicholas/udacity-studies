using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Door : MonoBehaviour 
{
    // Create a boolean value called "locked" that can be checked in Update() 
	public static bool locked = true;
	public static bool holdsKey = false;

	public AudioClip doorLockedSound;
	public AudioClip doorOpenedSound;
	public AudioSource doorAudioSource;


	void Start()
	{
		Debug.Log ($"Does the user hold the key? {holdsKey}");
		Debug.Log ($"Is the door locked? {locked}");
	}

	void Update()
	{
		if (!locked && holdsKey && transform.position.y <= 11f) {
			// Animate the door raising up
			transform.Translate (0, 600f * Time.deltaTime, 0, Space.World);
		}
	}

    public void Unlock()
    {
		if (holdsKey)
		{
			locked = false;
			doorAudioSource.clip = doorOpenedSound;
			doorAudioSource.Play ();
		}
		else
		{
			doorAudioSource.clip = doorLockedSound;
			doorAudioSource.Play ();
			Debug.Log ("User doesn't have a key!");
		}
	}
}
