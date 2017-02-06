using UnityEngine;
using System.Collections;

public class GameLogic : MonoBehaviour {
	public GameObject player;
	public GameObject startUI, restartUI;
	public GameObject startPoint, playPoint, restartPoint;

	public bool playerWon = false;

	// Use this for initialization
	void Start () 
	{
		player.transform.position = startPoint.transform.position;
	}

	// Update is called once per frame
	void Update () 
	{
		if (Input.GetMouseButtonDown (0) && player.transform.position==playPoint.transform.position) {
			puzzleSuccess ();
		}
	}

	//Begin the puzzle sequence
	public void startPuzzle()
	{
		toggleUI();
		iTween.MoveTo (player, iTween.Hash 
			(
				"position", playPoint.transform.position, 
				"time", 2, 
				"easetype", "linear"
			)
		);

	}

	//Reset the puzzle sequence
	public void resetPuzzle()
	{
		player.transform.position = startPoint.transform.position;
		toggleUI ();
	}

	//Do this when the player gets it right
	public void puzzleSuccess()
	{
		iTween.MoveTo (player, 
			iTween.Hash (
				"position", restartPoint.transform.position, 
				"time", 2, 
				"easetype", "linear"
			)
		);
	}
	public void toggleUI()
	{
		startUI.SetActive (!startUI.activeSelf);
		restartUI.SetActive (!restartUI.activeSelf);
	}

}