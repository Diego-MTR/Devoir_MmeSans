package com.example.demo.repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import com.example.demo.model.Cours;

public interface CoursRepository extends JpaRepository<Cours, Long> {
    List<Cours> findByMatiereContainingIgnoreCase(String matiere);
}
