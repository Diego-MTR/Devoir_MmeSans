package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.example.demo.repository.CoursRepository;
import com.example.demo.model.Cours;
import java.util.List;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestParam;

@RestController
@RequestMapping("/cours")
public class CoursController {

    private final CoursRepository coursRepository;

    public CoursController(CoursRepository coursRepository) {
        this.coursRepository = coursRepository;
    }

    @GetMapping
    public List<Cours> getAll() {
        return coursRepository.findAll();
    }

    @PostMapping
    public Cours addCours(@RequestBody Cours cours) {
        return coursRepository.save(cours);
    }

    @DeleteMapping("/{id}")
    public void deleteCours(@PathVariable Long id) {
        coursRepository.deleteById(id);
    }

    @GetMapping("/search")
    public List<Cours> search(@RequestParam String matiere) {
        return coursRepository.findByMatiereContainingIgnoreCase(matiere);
    }
}
