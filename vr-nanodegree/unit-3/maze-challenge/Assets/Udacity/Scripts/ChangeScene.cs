using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.SceneManagement;

public class ChangeScene : MonoBehaviour {

	public void GoToMazeScene()
	{
		Debug.Log ("Loading the Maze Scene");
		SceneManager.LoadScene("Maze");
	}

	public void GoToTempleScene()
	{
		Debug.Log ("Loading the Temple Scene");
		SceneManager.LoadScene("MazeComplete");
	}
}
